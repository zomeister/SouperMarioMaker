import React from 'react';
import Button from './Button';

export default function SoupCard({ name, image, onAddToFavorites, onRemoveFromFavorites, isFavorite }) {
    return (
        <div>
            <h1>Soup Card</h1>
            <p>{name}</p>
            <img src={image} alt="No image" />
            <Button
                handleClick={isFavorite ? onRemoveFromFavorites : onAddToFavorites}
                text={isFavorite ? "Remove from Favorites" : "Add to Favorites"}
            />
        </div>
    )
}