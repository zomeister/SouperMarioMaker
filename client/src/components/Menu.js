import IngredientCard from "./IngredientCard"

export default function Menu({ingredients}) {

    function renderIngredients(ingredients) {
        return ingredients.map(ingredient => 
            <IngredientCard key={ingredient.id} info={ingredient} name={ingredient.name} />)
    }


    return (
        <div>
            <h1>Menu</h1>
            <ul>{renderIngredients(ingredients) }</ul>
        </div>
    )
}