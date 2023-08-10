import React from 'react';
import IngredientCard from "./IngredientCard";
import SoupCard from "./SoupCard";

export default function Menu({ ingredients, soups, onAddToFavorites, onRemoveFromFavorites, favoriteSoups }) {
    function renderIngredients(ingredients) {
        return ingredients.map(ingredient => 
            <IngredientCard key={ingredient.id} info={ingredient} name={ingredient.name} />)
    }

    function renderSoups(soups) {
        return soups.map((soup, index) =>
            <SoupCard
                key={index}
                name={soup.name}
                image={soup.image}
                onAddToFavorites={() => onAddToFavorites(soup)}
                onRemoveFromFavorites={() => onRemoveFromFavorites(index)}
                isFavorite={favoriteSoups.some(favSoup => favSoup.name === soup.name)}
            />
        )
    }

    return (
        <div>
            <h1>Menu</h1>
            <ul>{renderIngredients(ingredients)}</ul>
            <ul>{renderSoups(soups)}</ul>
        </div>
    )
}