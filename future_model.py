from sklearn.preprocessing import MultiLabelBinarizer

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)





# Assuming you have a DataFrame called 'model_df' with 'gender_M' and 'gender_O' columns

model_df = merged_df.copy()

# Display the first 5 rows
print(model_df.head().to_markdown(index=False, numalign="left", stralign="left"))

# Print the column names and their data types
print(model_df.info())

# Drop rows with null values in specified columns (if needed)
model_df.dropna(subset=['age', 'became_member_on', 'income'], inplace=True)  # Removed 'gender' from subset

# Replace missing values in 'channels' with empty lists
model_df['channels'] = model_df['channels'].apply(lambda x: [] if isinstance(x, float) else x)

# One-hot encode 'channels'
mlb = MultiLabelBinarizer()
channel_encoded = mlb.fit_transform(model_df['channels'])
channel_df = pd.DataFrame(channel_encoded, columns=mlb.classes_)
model_df = pd.concat([model_df, channel_df], axis=1)
model_df.drop(columns=['channels'], inplace=True)

model_df.dropna(subset=['gender_O', 'gender_M'], inplace=True)

model_df['gender_O'] = model_df['gender_O'].astype(int)
model_df['gender_M'] = model_df['gender_M'].astype(int) 

# Convert `became_member_on` to datetime (if needed)
model_df['became_member_on'] = pd.to_datetime(model_df['became_member_on'])

# Extract year, month, and day from `became_member_on` (if needed)
model_df['became_member_year'] = model_df['became_member_on'].dt.year
model_df['became_member_month'] = model_df['became_member_on'].dt.month
model_df['became_member_day'] = model_df['became_member_on'].dt.day

# Drop the `became_member_on` column (if needed)
model_df.drop(columns=['became_member_on'], inplace=True)


# Scale the specified columns using StandardScaler
scaler = StandardScaler()
model_df[['age', 'income', 'difficulty', 'duration']] = scaler.fit_transform(
    model_df[['age', 'income', 'difficulty', 'duration']]
)

print(list(model_df.columns))
# Split the data into features (X) and target variable (y)
X = model_df.drop(columns=['offer_completed'])  # Assuming 'completed_offer' is your target
y = model_df['offer_completed']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


for col in X_train.columns:
    if X_train[col].dtype == 'object':
        print(f"Column '{col}' has non-numeric values:")
        print(X_train[col].unique()) 
# Train a logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)


# Predict on the testing set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')