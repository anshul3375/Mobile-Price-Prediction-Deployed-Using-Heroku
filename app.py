# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the Random Forest CLassifier model
filename = 'mobile_price_prediction_model.pkl'
regressor = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    brand_array = list()
    ram_array = list()
    rom_array = list()
    screen_type_array = list()
    front_camera_array = list()
    rear_camera_array = list()
    battery_mAh_array = list()
    mobile_array = list()
    
    if request.method == 'POST':
        
        mobile_brand = request.form['mobile-brand']
        if mobile_brand == 'Name_Apple':
            brand_array = brand_array + [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif mobile_brand == 'Name_Asus':
            brand_array = brand_array + [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif mobile_brand == 'Name_Google':
            brand_array = brand_array + [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif mobile_brand == 'Name_HTC':
            brand_array = brand_array + [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif mobile_brand == 'Name_Honor':
            brand_array = brand_array + [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif mobile_brand == 'Name_Huawei':
            brand_array = brand_array + [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]
        elif mobile_brand == 'Name_LG':
            brand_array = brand_array + [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]
        elif mobile_brand == 'Name_Mi':
            brand_array = brand_array + [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]
        elif mobile_brand == 'Name_Micromax':
            brand_array = brand_array + [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]
        elif mobile_brand == 'Name_Moto':
            brand_array = brand_array + [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]
        elif mobile_brand == 'Name_Motorola':
            brand_array = brand_array + [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]
        elif mobile_brand == 'Name_Nokia':
            brand_array = brand_array + [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]
        elif mobile_brand == 'Name_OPPO':
            brand_array = brand_array + [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0]
        elif mobile_brand == 'Name_OnePlus':
            brand_array = brand_array + [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0]
        elif mobile_brand == 'Name_Realme':
            brand_array = brand_array + [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]
        elif mobile_brand == 'Name_Redmi':
            brand_array = brand_array + [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]
        elif mobile_brand == 'Name_Samsung':
            brand_array = brand_array + [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]
        elif mobile_brand == 'Name_Vivo':
            brand_array = brand_array + [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
                    
         
            
        ram_type = request.form['ram-type']
        if ram_type == 'RAM_2 GB':
            ram_array = ram_array + [1,0,0,0,0,0]
        elif ram_type == 'RAM_3 GB':
            ram_array = ram_array + [0,1,0,0,0,0]
        elif ram_type == 'RAM_4 GB':
            ram_array = ram_array + [0,0,1,0,0,0]
        elif ram_type == 'RAM_6 GB':
            ram_array = ram_array + [0,0,0,1,0,0]
        elif ram_type == 'RAM_8 GB':
            ram_array = ram_array + [0,0,0,0,1,0]
        elif ram_type == 'RAM_12 GB':
            ram_array = ram_array + [0,0,0,0,0,1]  
            
            
        rom_type = request.form['rom-type']
        if rom_type == 'ROM_32 GB':
            rom_array = rom_array + [1,0,0,0,0]
        elif rom_type == 'ROM_64 GB':
            rom_array = rom_array + [0,1,0,0,0]
        elif rom_type == 'ROM_128 GB':
            rom_array = rom_array + [0,0,1,0,0]
        elif rom_type == 'ROM_256 GB':
            rom_array = rom_array + [0,0,0,1,0]
        elif rom_type == 'ROM_512 GB':
            rom_array = rom_array + [0,0,0,0,1]
            
            
            
        Screen_size_in_inch = float(request.form['Screen_size_in_inch'])
            
            
        rear_camera_type = request.form['rear_camera_type']
        if rear_camera_type == 'Rear_camera_in_MP_12MP':
            rear_camera_array = rear_camera_array + [1,0,0,0,0,0,0,0,0,0]
        elif rear_camera_type == 'Rear_camera_in_MP_12.3MP':
            rear_camera_array = rear_camera_array + [0,1,0,0,0,0,0,0,0,0]
        elif rear_camera_type == 'Rear_camera_in_MP_13MP':
            rear_camera_array = rear_camera_array + [0,0,1,0,0,0,0,0,0,0]
        elif rear_camera_type == 'Rear_camera_in_MP_16MP':
            rear_camera_array = rear_camera_array + [0,0,0,1,0,0,0,0,0,0]
        elif rear_camera_type == 'Rear_camera_in_MP_20MP':
            rear_camera_array = rear_camera_array + [0,0,0,0,1,0,0,0,0,0]
        elif rear_camera_type == 'Rear_camera_in_MP_24MP':
            rear_camera_array = rear_camera_array + [0,0,0,0,0,1,0,0,0,0]
        elif rear_camera_type == 'Rear_camera_in_MP_25MP':
            rear_camera_array = rear_camera_array + [0,0,0,0,0,0,1,0,0,0]
        elif rear_camera_type == 'Rear_camera_in_MP_32MP':
            rear_camera_array = rear_camera_array + [0,0,0,0,0,0,0,1,0,0]
        elif rear_camera_type == 'Rear_camera_in_MP_48MP':
            rear_camera_array = rear_camera_array + [0,0,0,0,0,0,0,0,1,0]
        elif rear_camera_type == 'Rear_camera_in_MP_64MP':
            rear_camera_array = rear_camera_array + [0,0,0,0,0,0,0,0,0,1]  
        
        
        front_camera_type = request.form['front_camera_type']
        if front_camera_type == 'Front_camera_in_MP_5MP':
            front_camera_array = front_camera_array + [1,0,0,0,0,0,0,0,0]
        elif front_camera_type == 'Front_camera_in_MP_7MP':
            front_camera_array = front_camera_array + [0,1,0,0,0,0,0,0,0]
        elif front_camera_type == 'Front_camera_in_MP_8MP':
            front_camera_array = front_camera_array + [0,0,1,0,0,0,0,0,0]
        elif front_camera_type == 'Front_camera_in_MP_13MP':
            front_camera_array = front_camera_array + [0,0,0,1,0,0,0,0,0]
        elif front_camera_type == 'Front_camera_in_MP_16MP':
            front_camera_array = front_camera_array + [0,0,0,0,1,0,0,0,0]
        elif front_camera_type == 'Front_camera_in_MP_20MP':
            front_camera_array = front_camera_array + [0,0,0,0,0,1,0,0,0]
        elif front_camera_type == 'Front_camera_in_MP_25MP':
            front_camera_array = front_camera_array + [0,0,0,0,0,0,1,0,0]
        elif front_camera_type == 'Front_camera_in_MP_32MP':
            front_camera_array = front_camera_array + [0,0,0,0,0,0,0,1,0]
        elif front_camera_type == 'Front_camera_in_MP_48MP':
            front_camera_array = front_camera_array + [0,0,0,0,0,0,0,0,1]
        
                    
            
        battery_mAh_type = float(request.form['battery_mAh_type'])


        
        mobile_array = brand_array + ram_array + rom_array + screen_type_array + [Screen_size_in_inch] + rear_camera_array + front_camera_array + [battery_mAh_type]
        
        data = np.array([mobile_array])
        my_prediction = int(regressor.predict(data)[0]) 
        my_prediction = my_prediction*1000 + 999
              
        return render_template('result.html', price = my_prediction)



if __name__ == '__main__':
	app.run(debug=True)
