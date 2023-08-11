import { useState, useEffect } from "react"
import IngredientCard from "./IngredientCard"

export default function Menu({soup, ingredients, soupIngredients} ) {

    const [soup_id, setSoup_id] = useState(1)
    const [activeIngredients, setActiveIngredients] = useState([])
    
    function handleDelete(iId) {
        const filteredList = activeIngredients.filter(item => item.id=== iId)
        for (let i = 0; i < filteredList.length; i++) {
            removeSoupIngredient(filteredList[i].id)
        }
    }
    
    function addSoupIngredient(iId) {
        const url = `http://localhost:3000/soup_ingredients`
        
        const data = {
            soup_id: soup_id,
            ingredient_id: iId,
            name: 'ingredients[iId].name'
        }

        try {
            fetch(url, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(data)
            })
            .then(r => r.json())
            .then(newSI => setActiveIngredients([...activeIngredients, newSI]))

        } catch (error) {
            console.log(error)
            console.log('caugth')
        }
    }
    
    function removeSoupIngredient(iId) {
        const url = `http://localhost:3000/soup_ingredients/${iId}`
    
        try {
            fetch(url, {
                method: "DELETE",
            })
            .then(r => r.json())
            .then(newSI => console.log(newSI))
        } catch (error) {
            console.log(error)
            console.log('caugth')
        }
        setActiveIngredients(activeIngredients.filter(ing => ing.name !== ingredients[iId].name))
    }

    function submitOrder() {

    }

    return (
        <div>
            <h1>Menu</h1>
            <ul>{ingredients.map(ingredient => 
                <IngredientCard key={ingredient.id} ingredient={ingredient} addSoupIngredient={addSoupIngredient} removeSoupIngredient={removeSoupIngredient}/>)}
            </ul>
            {/* name the soup first, then adds to api/soups */}
            <button onClick={()=>{}}>Save Soup</button> {/* patch to soupingredients db */}
        </div>
    )
}