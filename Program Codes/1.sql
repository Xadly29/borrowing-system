Create database FinalProject;
use FinalProject;

-- Create usertbl
CREATE TABLE IF NOT EXISTS usertbl (
    studentid INT PRIMARY KEY,
    studentname VARCHAR(255) NOT NULL,
    studentpassword VARCHAR(255) NOT NULL, -- Password should be hashed before storage
    studentemail VARCHAR(255) NOT NULL
    -- Add other user information fields as needed
);

-- Create itemtbl
CREATE TABLE IF NOT EXISTS itemtbl (
    itemID INT AUTO_INCREMENT PRIMARY KEY,
    itemCategory VARCHAR(100),
    itemClass VARCHAR(100),
    Quantity INT,
    itemDescription TEXT,
    DateAquired DATE,
    remarks VARCHAR(255),
    
    availability ENUM('available', 'unavailable') DEFAULT 'available'
    -- Add other item information fields as needed
);

-- Create historytbl
CREATE TABLE IF NOT EXISTS historytbl (
    historyID INT AUTO_INCREMENT PRIMARY KEY,
    studentid INT,
    itemID INT,
    dateBorrowed DATE, 
    status ENUM('borrowed', 'returned') NOT NULL
    -- Add other history information fields as needed
);

ALTER TABLE historytbl
ADD CONSTRAINT fk_userID FOREIGN KEY (studentid) REFERENCES usertbl(studentid);

ALTER TABLE historytbl
ADD CONSTRAINT fk_itemID FOREIGN KEY (itemID) REFERENCES itemtbl(itemID);

