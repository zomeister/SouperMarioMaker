import { useState } from'react'
import Button from './Button'

export default function IngredientCard({info}) {
    const [inSoup, setInSoup] = useState(false)

    function removeIngredient() {
        setInSoup(prev => !prev)
        // patch to soup/<id>/ingredients
        console.log('remove ingredient')
    }
    
    function addIngredient() {
        setInSoup(prev => !prev)
        // delete to soup/<id>/ingredients
        console.log('add ingredient')
    }

    return (
        <li><em>{info.name}</em>
            {/* <p>{info.description}</p> */}
            {/* <p>{info.price}</p> */}
            <Button 
                handleClick={inSoup ? removeIngredient : addIngredient} 
                text= {inSoup ? 'Remove': 'Add'}
            ></Button>
        </li>
    )
}