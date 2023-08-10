import React from "react"
export default function FavoriteSoups({ favoriteSoups, onRemoveFromFavorites }) {

    
    return ( 
            favoriteSoups.map((soup, index) => (
                <div >
          <div className='max-w-lg w-full lg:max-w-full lg:flex'>
            <div
              className='h-55 lg:h-auto lg:w-44 flex-none bg-cover rounded-t lg:rounded-t-none lg:rounded-l text-center overflow-hidden'
              style={{
                backgroundImage: `url(${soup.image})`,
              }}
              title='Image Title'
            ></div>
            <div className='border-r border-b border-l border-gray-400 lg:border-l-0 lg:border-t lg:border-gray-400 bg-white rounded-b lg:rounded-b-none lg:rounded-r p-4 flex flex-col justify-between leading-normal'>
              <div className='mb-8'>
                <div className='text-gray-900 font-bold text-xl mb-2'>
                  {soup.name}
                </div>
              </div>
              <button onClick={() => onRemoveFromFavorites(index)}>
                Remove
                </button>
            </div>
          </div>
        </div>
      ))
    )}

