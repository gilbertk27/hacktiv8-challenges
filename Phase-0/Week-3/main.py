from fastapi import FastAPI, HTTPException, Header
import pandas as pd
import uvicorn

# Load data csv yang sudah diolah dengan pandas, kemudian konversi data ke dictionary `df.to_dict()` 
# atau json `df.to_json()` untuk dapat diolah lebih lanjut dengan API menggunakan FastAPI.

app = FastAPI()

API_KEY = "phase0h8"

df = pd.read_csv('data_cleaned.csv')
data = df.to_dict()

@app.get("/")
def root():
    return {"message":"Welcome to Toko H8 Shopping Cart! There are some features that you can explore",
            "menu":{1:"See data (/show)",
                    2:"Delete data (/del/id)"}}

@app.get("/show")
def show():
    return data

@app.post("/add")
def add_item(added_item:int, api_key: str = Header(None)):
    if api_key is None or api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key. You are not allowed to add data!")
    else:
        id = len(data["duration_sec"].keys())+1
        data[id] = added_item
        # data['duration_sec'].append(added_item['minutes']) #kalo data dictionary
        return f"Item successfully added into your cart with ID {id}"

# delete based value 
# @app.delete("/del/{value}")
# def remove_row(inp_value:str, api_key: str = Header(None)):
#     for key,value in enumerate(data['duration_sec']):
#         if value == inp_value:
#             raise HTTPException(status_code=404, detail=f"Item with ID {id} not found")
#         else:
#             if api_key is None or api_key != API_KEY:
#                 raise HTTPException(status_code=401, detail="Invalid API Key. You are not allowed to delete data!")
#             else:
#                     if value == inp_value:
#                         data['duration_sec'].pop(key)
#                     return {"message": f"{inp_value} has been deleted successfully."}
                
        
@app.delete("/delete_data/{index}")
async def delete_data(index: int, api_key: str = Header(None)):
    if index not in data['duration_sec'].keys():
        raise HTTPException(status_code=404, detail=f"Item with ID {index} not found")
    else:
        if api_key is None or api_key != API_KEY:
            raise HTTPException(status_code=401, detail="Invalid API Key. You are not allowed to delete data!")
        else:
            data["duration_sec"].pop(index)
            return {"message": f"Item with ID {index} has been deleted successfully."}

        