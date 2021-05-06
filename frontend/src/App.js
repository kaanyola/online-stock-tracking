import React from "react";
import Home from "./components/Home";
import Products from "./components/Products";
import Sellers from "./components/Sellers";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import Button from "react-bootstrap/Button";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import axios from "axios";

export default class App extends React.Component {
  render() {
    return (
      <Router>
        <Navbar bg="dark" variant="dark" className="mb-2">
          <Navbar.Brand href="#home"> Navbar </Navbar.Brand>{" "}
          <Nav className="mr-auto">
            <Nav.Link href="home"> Home </Nav.Link>{" "}
            <Nav.Link href="/products"> Products </Nav.Link>{" "}
            <Nav.Link href="/sellers"> Sellers </Nav.Link>{" "}
          </Nav>{" "}
        </Navbar>
        <div>
          {/* A <Switch> looks through its children <Route>s and
                    renders the first one that matches the current URL. */}{" "}
          <Switch>
            <Route path="/products">
              <Products />
            </Route>{" "}
            <Route path="/sellers">
              <Sellers />
            </Route>{" "}
          </Switch>{" "}
        </div>{" "}
      </Router>
    );
  }
}
