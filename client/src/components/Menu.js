import IngredientCard from "./IngredientCard"
import React, { useState} from "react"





export default function Menu({soups, setSoups}) {

    const [name, setName] = useState('')
    const [image, setImage] = useState('')

    const handleName = (e) => {setName(e.target.value)}

    const handleImage = (e) => {setImage(e.target.value)}
    
    const handleSubmit = (event) => {
        event.preventDefault();
        const newSoup = {
            name: name,
            image: image,
        }
        setSoups([...soups, newSoup])
        fetch("http://localhost:5555/soups", {
            method: "POST", 
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(newSoup)
        })
        .then(resp => {
            if(resp.ok){
                console.log("Everything is cool")
            }
            else{
                resp.json().then((missing) => {
                    console.log(missing)
                })
            }
        })
    }
        return (
            <div className="new-soup-form">
              <h2>Soup Maker</h2>
              <form onSubmit={handleSubmit}>
                <input type="text" name="name" placeholder={name} onChange={handleName}/>
                <input type="text" name="image" placeholder={image}  onChange={handleImage}/>
                <button type="submit">Add Soup</button>
              </form>
            </div>
          );

}
