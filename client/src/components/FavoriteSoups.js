import React from "react"
export default function FavoriteSoups({ favoriteSoups, onRemoveFromFavorites }) {
    return (
        <div>
            <h1>Favorites</h1>
            <ul>
                {favoriteSoups.map((soup, index) => (
                    <li key={index}>
                        {soup.name}
                        <img src={soup.image}     />
                        <button onClick={() => onRemoveFromFavorites(index)}>
                            Remove
                        </button>
                    </li>
                ))}
            </ul>
        </div>
    );
}