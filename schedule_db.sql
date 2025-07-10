-- Таблица студентов
CREATE TABLE Students (
    StudentID INT PRIMARY KEY IDENTITY,
    FullName NVARCHAR(100),
    GroupName NVARCHAR(50)
);

-- Таблица предметов
CREATE TABLE Subjects (
    SubjectID INT PRIMARY KEY IDENTITY,
    SubjectName NVARCHAR(100),
    Lecturer NVARCHAR(100)
);

-- Таблица расписания (переменная информация)
CREATE TABLE Schedule (
    ScheduleID INT PRIMARY KEY IDENTITY,
    StudentID INT,
    SubjectID INT,
    Day NVARCHAR(20),
    Time NVARCHAR(10),
    Room NVARCHAR(20),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (SubjectID) REFERENCES Subjects(SubjectID)
);
