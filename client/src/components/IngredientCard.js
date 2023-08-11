import { useState } from'react'
import Button from './Button'

export default function IngredientCard({ingredient, addSoupIngredient, removeSoupIngredient }) {
    
    const [inSoup, setInSoup] = useState(false)
    const { name, image } = ingredient

    function handleDelete(id) {
        // const filteredList = list.filter(item => item.id!== id)
        // for (let i = 0; i < filteredList.length; i++) {
        //     removeSoupIngredient(filteredList[i].id)
        // }
    }

    function handleToggle(e) {
        if (inSoup) {
            handleDelete(ingredient.id)
        } else {
            addSoupIngredient(ingredient.id)
        }
        setInSoup(prev => !prev)
    }

    return (
        <li><em>{name}</em>
            <img src={image} alt={name}></img>
            <button onClick={(e) => handleToggle(e)}>{inSoup ? 'Remove': 'Add'}</button>
        </li>
    )
}