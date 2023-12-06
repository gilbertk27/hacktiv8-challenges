
'''
=================================================
Graded Challenge 3

Nama  : Gilbert Kurniawan H
Batch : RMT-26

Program ini dibuat untuk pembuatan API dengan fungsionalitas memperlihatkan, menabah, mengedit, dan menghapus data.
=================================================
'''

from fastapi import FastAPI, HTTPException, Header
import pandas as pd

app = FastAPI()

API_KEY = "phase0h8"

df = pd.read_csv('result.csv')
data = df.to_dict()

# data = {"name":"shopping cart",
#         "columns":["prod_name","price","num_items"],
#         "items":{}}

@app.get("/")
def root():
    return {"message":"Welcome to Toko H8 Shopping Cart! There are some features that you can explore",
            "menu":{1:"See shopping cart (/data)",
                    2:"Add item (/add) - You may need request",
                    3:"Edit shopping cart (/edit/id)",
                    4:"Delete item from shopping cart (/del/id)"}}

@app.get("/cart") #kalo ngga mau diubah data asliny langsung -> ke mas yuda
def show():
    return df.to_dict()

@app.get("/cart_converted")
def show():
    return data

@app.post("/add_example") #tambah pake multiple dictionary -> contoh data comment
def add_item(added_item:dict, api_key: str = Header(None)):
    if api_key is None or api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key. You are not allowed to add data!")
    else:
        id = len(data["duration_sec"].keys())+1
        data["duration_sec"][id] = added_item
        return f"Item successfully added into your cart with ID {id}"
    
@app.post("/add_masyuda") #tambah pake dictionary
def handlerPost(added_item:dict):
    df.loc[len(df['duration_sec'])] = added_item['minute']
    id = len(df['duration_sec'])
    return  f"berhasil adding data di ID {id}"

@app.post("/add_gil") #tambah pake int aja
def add_item(added_item:int, api_key: str = Header(None)):
    if api_key is None or api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key. You are not allowed to add data!")
    else:
        id = len(data["duration_sec"].keys())+1
        data[id] = added_item
        # data['duration_sec'].append(added_item['minutes']) #kalo data dictionary
        return f"Item successfully added into your cart with ID {id}"

@app.put("/edit/{id}")
def update_cart(id:int,updated_cart:dict, api_key: str = Header(None)):
    if id not in data['duration_sec'].keys():
        raise HTTPException(status_code=404, detail=f"Item with ID {id} not found")
    else:
        if api_key is None or api_key != API_KEY:
            raise HTTPException(status_code=401, detail="Invalid API Key. You are not allowed to edit data!")
        else:
            data["duration_sec"][id].update(updated_cart)
            return {"message": f"Item with ID {id} has been updated successfully."}

@app.delete("/del/{id}")
def remove_row(id:int, api_key: str = Header(None)):
    if id not in df['duration_sec'].keys():
        raise HTTPException(status_code=404, detail=f"Item with ID {id} not found")
    else:
        if api_key is None or api_key != API_KEY:
            raise HTTPException(status_code=401, detail="Invalid API Key. You are not allowed to delete data!")
        else:
            df["duration_sec"].pop(id)
            return {"message": f"Item with ID {id} has been deleted successfully."}