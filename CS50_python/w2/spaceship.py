
def main():
    spaceship ={
        "name" : "my spaceship",

    }
    spaceship.update( {"distance" : "1800 km", "age" : "54",} )
    print(create_report(spaceship))






def create_report(ship):
    return f"""

    ========  REPORT  ==========

    name: {ship["name"]}
    distance: {ship.get("distance", "not found")}
    age: {ship["age"]}
    title: {ship.get("title", "none")}

    ===========================

    """

main()
