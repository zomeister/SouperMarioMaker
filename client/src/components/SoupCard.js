import Button from './Button'
import React from 'react'

export default function SoupCard({ name, image, onAddToFavorites, onRemoveFromFavorites, isFavorite }) {


    function submitOrder(e) {
        console.log('submitOrder');
    }
    


    
    return (
        <div >
          <div className='max-w-lg w-full lg:max-w-full lg:flex flex-shrink' style={{ height: '200px'}}>
            <div
              className='h-44 lg:h-auto lg:w-44 flex-none  bg-cover rounded-t lg:rounded-t-none lg:rounded-l text-center overflow-hidden'
              style={{ backgroundImage: `url(${image})`, height: '100%' }}
              title='Image Title'
            ></div>
            <div className='border-r border-b border-l border-gray-400 lg:border-l-0 lg:border-t lg:border-gray-400 bg-white rounded-b lg:rounded-b-none lg:rounded-r p-4 flex flex-col justify-between leading-normal' >
              <div className='mb-8'>
                <div className='text-gray-900 font-bold text-xl mb-2'>
                  {name}
                </div>
              </div>
              <Button
                handleClick={isFavorite ? onRemoveFromFavorites : onAddToFavorites}
                text={isFavorite ? "Remove from Favorites" : "Add to Favorites"}
          ></Button>
            </div>
          </div>
        </div>
      );
    }
