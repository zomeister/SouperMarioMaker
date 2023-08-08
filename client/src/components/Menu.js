import IngredientCard from "./IngredientCard"

export default function Menu({soup_id, ingredients}) {
    

    return (
        <div>
            <h1>Menu</h1>
            <ul>
                {ingredients.map(ingredient => 
                    <IngredientCard 
                        key={ingredient.id} 
                        info={ingredient} />)}
            </ul>
        </div>
    )
}