import React, { useEffect, useState } from "react";
import Button from "./Button";
import FavoriteSoups from "./FavoriteSoups";
import IngredientCard from "./IngredientCard";
import Menu from "./Menu";
import SoupCard from "./SoupCard";
import { Switch, Route} from "react-router-dom";
import { BrowserRouter } from "react-router-dom/cjs/react-router-dom.min";
import Header from "./Header";
import Home from "./Home";
import TheSoups from "./TheSoups";


function App() {
  // const [soups, setSoups] = useState(null);
  const [currentSoup, setCurrentSoup] = useState(null);

  const [ingredients, setIngredients] = useState([]) 
  const [soups, setSoups] = useState([]);
  const [favoriteSoups, setFavoriteSoups] = useState([]);

  useEffect(() => {
    fetchIngredients();
  }, []);

  function fetchIngredients() {
    fetch('http://localhost:5555/ingredients')
    .then((res) => res.json())
    .then((ingredients) => setIngredients(ingredients))
  }
  console.log(ingredients);


  useEffect(() => {
    fetchAllSoups();
  }, []);

  function fetchAllSoups() {
  fetch('http://localhost:5555/soups')
  .then(res => res.json())
  .then(soups => setSoups(soups))
  console.log(soups)
  }

  function handleAddToFavorites(soup) {
    
        setFavoriteSoups([...favoriteSoups, soup]);
    
      }
    
        function handleRemoveFromFavorites(index) {
    
            const updatedFavorites = [...favoriteSoups];
    
            updatedFavorites.splice(index, 1);
    
            setFavoriteSoups(updatedFavorites);
    
        }

  return ( <BrowserRouter>
  <>
      <div className="App">
      </div>
      <div className="App2">
      <h1 id="head"><a id='heada' href="#0" className="font-mario font-normal text-lg">SOUPER MARIO MAKER</a></h1>
        <Switch>
          <Route exact path="/">
            <Header/>
            <Home/>   
          </Route>
          <Route exact path="/thesoups">
          <Header/>
          <TheSoups
                soups={soups}
                onAddToFavorites={handleAddToFavorites}
                onRemoveFromFavorites={handleRemoveFromFavorites}
                favoriteSoups={favoriteSoups}
              />
          </Route>
          <Route exact path="/soupmaker">
            <Header/>
            <Menu soups={soups} setSoups={setSoups}/>
          </Route>
          <Route path="/favoritesoups">
            <Header/>
            <FavoriteSoups soups={soups} favoriteSoups={favoriteSoups} onRemoveFromFavorites={handleRemoveFromFavorites}/>
          </Route>
        </Switch>
      </div>
  </>
  </BrowserRouter>
  )
}



export default App;
