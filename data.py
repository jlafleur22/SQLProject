#Student Information Format = lastname, firstname, Gender, graduationYear
studentStart = [("Smith", "John", "M", '2030'),
                ("Ventura", "Ace", "M", '2030'),
                ("Balboa", "Rocky", "M", '2030'),
                ("Sands", "Hunter", "M", '2030'),
                ("Tarantino", "Quentin", "M", '2030'),
                ("Trejo", "Cucuy", "M", '2031'),
                ("Ajedrez", "Carolina", "F", '2031'),
                ("Frozenza", "Elsa", "F", '2031'),
                ("Weasely", "Duke", "M", '2031'),
                ("Spencer", "Lacey", "F", '2031'),
                ("McLain", "Jonathan", "M", '2032'),
                ("Yarborough", "Caitlin", "F", '2032'),
                ("Frozenza", "Olaf", "M", '2032'),
                ("Jackson", "Zeus", "M", '2032'),
                ("Kowalski", "Connie", "F", '2032'),
                ("Wiess", "Elizabeth", "F", '2033'),
                ("Frozenza", "Anna", "F", '2033'),
                ("Chu", "Rachel", "F", '2033'),
                ("Goh", "Piekh", "F", '2033'),
                ("Lee", "Araminta", "F", '2033')]

#Scholastic Year = StudentID, quarter, grade, test or quiz
scoresStart = [(1, 1, 92, "Q"),
            (1, 1, 91, "Q"),
            (1, 1, 95, "T"),
            (2, 1, 87, "Q"),
            (2, 1, 99, "Q"),
            (2, 1, 92, "T"),
            (3, 1, 99, "Q"),
            (3, 1, 101, "Q"),
            (3, 1, 85, "T"),
            (4, 1, 100, "Q"),
            (4, 1, 100, "Q"),
            (4, 1, 100, "T"),
            (5, 1, 79, "Q"),
            (5, 1, 76, "Q"),
            (5, 1, 73, "T"),
            (6, 1, 88, "Q"),
            (6, 1, 89, "Q"),
            (6, 1, 88, "T"),
            (7, 1, 99, "Q"),
            (7, 1, 89, "Q"),
            (7, 1, 95, "T"),
            (8, 1, 96, "Q"),
            (8, 1, 97, "Q"),
            (8, 1, 89, "T"),
            (9, 1, 99, "Q"),
            (9, 1, 98, "Q"),
            (9, 1, 99, "T"),
            (10, 1, 89, "Q"),
            (10, 1, 91, "Q"),
            (10, 1, 92, "T"),
            (11, 1, 91, "Q"),
            (11, 1, 91, "Q"),
            (11, 1, 89, "T"),
            (12, 1, 91, "Q"),
            (12, 1, 95, "Q"),
            (12, 1, 89, "T"),
            (13, 1, 96, "Q"),
            (13, 1, 91, "Q"),
            (13, 1, 89, "T"),
            (14, 1, 91, "Q"),
            (14, 1, 93, "Q"),
            (14, 1, 89, "T"),
            (15, 1, 91, "Q"),
            (15, 1, 92, "Q"),
            (15, 1, 89, "T"),
            (16, 1, 99, "Q"),
            (16, 1, 91, "Q"),
            (16, 1, 89, "T"),
            (17, 1, 91, "Q"),
            (17, 1, 97, "Q"),
            (17, 1, 89, "T"),
            (18, 1, 91, "Q"),
            (18, 1, 98, "Q"),
            (18, 1, 99, "T"),
            (19, 1, 91, "Q"),
            (19, 1, 91, "Q"),
            (19, 1, 91, "T"),
            (20, 1, 91, "Q"),
            (20, 1, 91, "Q"),
            (20, 1, 93, "T"),
            (1, 2, 90, "Q"),
            (1, 2, 93, "Q"),
            (1, 2, 95, "T"),
            (2, 2, 94, "Q"),
            (2, 2, 96, "Q"),
            (2, 2, 97, "T"),
            (3, 2, 97, "Q"),
            (3, 2, 98, "Q"),
            (3, 2, 99, "T"),
            (4, 2, 88, "Q"),
            (4, 2, 85, "Q"),
            (4, 2, 86, "T"),
            (5, 2, 82, "Q"),
            (5, 2, 84, "Q"),
            (5, 2, 83, "T"),
            (6, 2, 89, "Q"),
            (6, 2, 88, "Q"),
            (6, 2, 95, "T"),
            (7, 2, 99, "Q"),
            (7, 2, 97, "Q"),
            (7, 2, 99, "T"),
            (8, 2, 95, "Q"),
            (8, 2, 96, "Q"),
            (8, 2, 98, "T"),
            (9, 2, 94, "Q"),
            (9, 2, 93, "Q"),
            (9, 2, 94, "T"),
            (10, 2, 90, "Q"),
            (10, 2, 93, "Q"),
            (10, 2, 95, "T"),
            (11, 2, 90, "Q"),
            (11, 2, 93, "Q"),
            (11, 2, 95, "T"),
            (12, 2, 94, "Q"),
            (12, 2, 96, "Q"),
            (12, 2, 97, "T"),
            (13, 2, 97, "Q"),
            (13, 2, 98, "Q"),
            (13, 2, 99, "T"),
            (14, 2, 88, "Q"),
            (14, 2, 85, "Q"),
            (14, 2, 86, "T"),
            (15, 2, 82, "Q"),
            (15, 2, 84, "Q"),
            (15, 2, 83, "T"),
            (16, 2, 89, "Q"),
            (16, 2, 88, "Q"),
            (16, 2, 95, "T"),
            (17, 2, 99, "Q"),
            (17, 2, 97, "Q"),
            (17, 2, 99, "T"),
            (18, 2, 95, "Q"),
            (18, 2, 96, "Q"),
            (18, 2, 98, "T"),
            (19, 2, 94, "Q"),
            (19, 2, 93, "Q"),
            (19, 2, 94, "T"),
            (20, 2, 94, "Q"),
            (20, 2, 93, "Q"),
            (20, 2, 95, "T")]

transferStudent = [(21, 1, 99, "Q"),
                  (21, 1, 100, "Q"),
                  (21, 1, 100, "T"),
                  (21, 2, 100, "Q"),
                  (21, 2, 100, "Q"),
                  (21, 2, 100, "T")]