import React from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route
} from "react-router-dom";
import Home from './pages/home/home';
import Details from './pages/details/details';

function App() {
  return (
    <div className="container" style={{marginTop: 20 + 'px'}}>
      <Router>
        <Switch>
          <Route path="/details">
            <Details />
          </Route>
          <Route path="/">
            <Home />
          </Route>
        </Switch>
      </Router>
      
    </div>
  );
}

export default App;
