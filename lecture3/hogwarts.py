students=[
    {
        "name":"hermione",
        "house":"gryffindor",
        "paronus":"otter",
    },

    {
        "name":"harry",
        "house":"gryffindor",
        "paronus":"stag",
    },  

    {
        "name":"draco",
        "house":"slytherin",
        "paronus":None,
    },
]

for student in students:
    print(student["name"],student["house"],student["paronus"],sep="|")
