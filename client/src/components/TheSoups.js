import React from "react";
import SoupCard from "./SoupCard";

function TheSoups({soups, onAddToFavorites, onRemoveFromFavorites, favoriteSoups}){

    


    const theSoups = soups.map((soup, index) => 
    <SoupCard
        key={index}
        name={soup.name}
        image={soup.image}
        id={soup.id}
        onAddToFavorites={() => onAddToFavorites(soup)}
        onRemoveFromFavorites={() => onRemoveFromFavorites(index)}
        isFavorite={favoriteSoups.some(favSoup => favSoup.name === soup.name)}
    />
    )
    return (
        <div className='grid grid-cols-3 md:grid-cols-3 gap-10'>{theSoups}</div>
    )

}
export default TheSoups