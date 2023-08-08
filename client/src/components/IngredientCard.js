import { useState } from'react'
import Button from './Button'

export default function IngredientCard({name}) {
    const [inCart, setInCart] = useState(false)

    // function toggleIngredient() {
    //     setInCart(prev => !prev)
    //     // TODO: add/remove ingredient to current soup in db (PATCH)
    //     console.log('add ingredient')
    // }

    return (
        <li>
            <h1>{name}</h1>
            {/* <p>{info.description}</p> */}
            {/* <p>{info.price}</p> */}
            {/* <Button 
                handleClick={() => toggleIngredient} 
                text= {inCart ? 'Remove': 'Add'}
            ></Button> */}
        </li>
    )
}