import pandas as pd

def read_csv():
    try:
        file=r"C:\Users\kapil.tyagi_vvdntech\Desktop\CarService-main\CarService-main\src\CarData.csv"
        df = pd.read_csv(file)
        carData = f"""Car Data :  {df.to_string()}"""
        return carData
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")
        return {}
#car_data=read_csv()
#print(car_data)