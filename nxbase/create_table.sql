CREATE TABLE IF NOT EXISTS Affiliations (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	short_description TEXT UNIQUE,
	long_description TEXT
);
######
CREATE TABLE IF NOT EXISTS Roles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        role_type TEXT UNIQUE,
        role_description TEXT
);
######
CREATE TABLE IF NOT EXISTS NxBaseUsers (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
   	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	email TEXT UNIQUE,
	affiliation_id INTEGER,
	date_joined TEXT,	
	FOREIGN KEY (affiliation_id) REFERENCES Affiliations (id)
);
######
CREATE TABLE IF NOT EXISTS Modules (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
   	name TEXT NOT NULL,
	description TEXT NOT NULL,
	date_added TEXT,
	owner_id INTEGER,
	FOREIGN KEY (owner_id) REFERENCES NxBaseUsers(id)
);
######
CREATE TABLE IF NOT EXISTS UserModule (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       user_id INTEGER,
       module_id INTEGER,
       role_id INTEGER,
       FOREIGN KEY(user_id) REFERENCES users(id),
       FOREIGN KEY(module_id) REFERENCES modules(id),
       FOREIGN KEY(role_id) REFERENCES roles(id)
);
######
CREATE TABLE IF NOT EXISTS Questions (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       module_id INTEGER,
       short_text TEXT NOT NULL,
       details TEXT,
       type TEXT CHECK( Type IN ('multiple','single','text', 'code') ) NOT NULL,
       date_added TEXT,
       FOREIGN KEY(module_id) REFERENCES Modules(id)
);
######
CREATE TABLE IF NOT EXISTS Answers (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       text TEXT,
       correct INTEGER NOT NULL,
       explanation TEXT,       
       question_id INTEGER,
       FOREIGN KEY(question_id) REFERENCES Questions(id)
);
######
CREATE TABLE IF NOT EXISTS Hints (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       text TEXT NOT NULL,
       question_id INTEGER,
       FOREIGN KEY(question_id) REFERENCES Questions(id)
);
###### STARTING THE INSERTS ######
INSERT INTO Affiliations (short_description, long_description) 
       VALUES ("UH MANOA", "University of Hawaii at Manoa");
######
INSERT INTO Roles (role_type, role_description)
       VALUES ("OWNER", "Module owner or developer");
INSERT INTO Roles (role_type, role_description)
       VALUES ("EDITOR", "Module editor");
INSERT INTO Roles (role_type, role_description)
       VALUES ("STUDENT", "Student taking either registered on not registered for a module");
######
INSERT INTO NxBaseUsers (first_name, last_name, email, affiliation_id, date_joined)
       VALUES ("Mahdi", "Bel", "b.mahdi@gmail.com", 1, "1/1/2021");
INSERT INTO NxBaseUsers (first_name, last_name, email, affiliation_id, date_joined)
       VALUES ("John", "Doe", "j.doe@gmail.com", 1, "1/1/2021");
############### MODULE 1 ################
INSERT INTO Modules ( name, description, date_added, owner_id)
       VALUES ("INTRODUCTION TO PYTHON",
       	       "Basic introduction to Python for non-programmers",
	       "1/1/2020", 1);
######
INSERT INTO UserModule (user_id, module_id, role_id)
       VALUES (1, 1, 1);
INSERT INTO UserModule (user_id, module_id, role_id)
       VALUES (2, 1, 3);
######
INSERT INTO Questions ( module_id, short_text, details, type, date_added)
       VALUES (1,
       	       "Which of the following data types cannot be used as keys?",
	       "If in doubt, try creating an example dictionary with these types as keys and verify which ones are valid key data types.",
	       "multiple",
	       "01/01/2021"
	       );
INSERT INTO Hints(text, question_id)
       VALUES ("A dict key cannot be mutable.", 1);
INSERT INTO Answers (text, correct, explanation, question_id)
       VALUES ("Strings", 0, "Strings are hashable because they are non-mutable", 1);
INSERT INTO Answers (text, correct, explanation, question_id)
       VALUES ("Floats", 0, "Floats are hashable because they are non-mutable", 1);
INSERT INTO Answers (text, correct, explanation, question_id)
       VALUES ("Tuples", 0, "Tuples are hashable because they are non-mutable", 1);
INSERT INTO Answers (text, correct, explanation, question_id)
       VALUES ("List", 1, "lists are not hashable because they are mutable, i.e., they can be extended.", 1);
#####
INSERT INTO Questions ( module_id, short_text, details, type, date_added)
       VALUES (1,
               "Python lists can only contain one data type.",
               "Can a list contain both strings and ints?",
               "single",
               "01/01/2021"
	       );
INSERT INTO Hints(text, question_id)
       VALUES ("Recalling the difference between an array and a list may help", 2);
INSERT INTO Answers (text, correct, explanation, question_id)
       VALUES ("True", 0, "List can contains a mix of other data types", 2);
INSERT INTO Answers (text, correct, explanation, question_id)
       VALUES ("False", 1, "Correct!", 2);
############### MODULE 2 #################
INSERT INTO Modules ( name, description, date_added, owner_id)
       VALUES ("Data Wrangling in Python",
       	       "Data Wrangling intro wiht Pandas",
	       "1/1/2020", 1);
######
INSERT INTO UserModule (user_id, module_id, role_id)
       VALUES (1, 2, 1);
INSERT INTO UserModule (user_id, module_id, role_id)
       VALUES (2, 2, 3);
######
INSERT INTO Questions ( module_id, short_text, details, type, date_added)
       VALUES (2,
               "Which of the following statements will exclude from `flight_df` all flights that are missing both
	       `ARRIVAL\_DELAY` and `DEPARTURE\_DELAY`?",
               "| index |ORIGIN | DESTINATION | DEPARTURE_DELAY| ARRIVAL_DELAY |
	       |----------|-----------|---------|----------|----------|
	       | 0 | HNL | SFO | 3.0 | -21.0 |
	       | 1 | LAS | HNL | NaN | -2.0 |
	       | 2 | HNL | ITO | NaN | NaN |
	       | 3 | HNL | KOA| -6.0 | -9.0 |",
               "single",
               "01/01/2021"
	       );
INSERT INTO Hints(text, question_id)
       VALUES ("Recall that `&` mean `AND` while `|` means `OR`.", 3);
INSERT INTO Hints(text, question_id)
       VALUES ("Recall that a condition can be negated using `~`", 3);
INSERT INTO Answers (text, correct, explanation, question_id)
       VALUES ("`flights_df.dropna(axis='rows',thresh=2)`", 0, "dropna simple drop rows that have at least `thresh` missing values", 3);
INSERT INTO Answers (text, correct, explanation, question_id)
       VALUES ("`flights_df.loc[ ~flights_df.loc[:, 'DEPARTURE_DELAY'].isnull() | ~flights_df.loc[:, 'ARRIVAL_DELAY'].isnull(), :]`", 1, "Correct1", 3);
INSERT INTO Answers (text, correct, explanation, question_id)
       VALUES ("`flights_df.loc[ ~flights_df.loc[:, 'DEPARTURE_DELAY'].isnull() & ~flights_df.loc[:, 'ARRIVAL_DELAY'].isnull(), :]`", 0, "Recall that `|` means `OR`", 3);
######
INSERT INTO Questions ( module_id, short_text, details, type, date_added)
       VALUES (2,
               "Which of the following instructions creates a new series that is the average number of hits per game?",
               "To answer this question, consider the `DataFrame` `NCAA_batting_df` with the follwing fields.
	       | Column |Description|
	       |:----------|-----------|
	       | `Name` | Name of the team |
	       | `G` | Number of games played in the season  |
	       | `W.L` | Number of Wins-Number of Losses |
	       | `H` | Number of hits in total |
	       | `BA` | The teams batting average |",
	       "single",
               "01/01/2021"
               );
INSERT INTO Hints(text, question_id)
       VALUES ("", 3);
INSERT INTO Answers (text, correct, explanation, question_id)
       VALUES ("`NCAA_batting_df.loc[:, 'H' / 'G']`", 0, "The second index refers is the division of the letters 'H' and'G'. We cannot devide letters!", 3);
INSERT INTO Answers (text, correct, explanation, question_id)
       VALUES ("`NCAA_batting_df.loc['H', :] / NCAA_batting_df.loc['G', :]`", 0, "The first index refers to the row. Recall that `loc` refes columns ", 3);
INSERT INTO Answers (text, correct, explanation, question_id)
       VALUES ("`NCAA_batting_df.loc[:, 'H'] / NCAA_batting_df.loc[:, 'G']`", 1, "There are not column with titles `H` and `G`", 3);
INSERT INTO Answers (text, correct, explanation, question_id)
       VALUES ("None of the above", 1, "Correct!", 3);
