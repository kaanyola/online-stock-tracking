import React from 'react';

import axios from 'axios';

export default class Sellers extends React.Component {
  state = {
    persons: []
  }

  componentDidMount() {
    axios.get(`http://127.0.0.1:8000/api/saticilar/`)
      .then(res => {
        const persons = res.data;
        this.setState({ persons });
      })
  }

  render() {
    return (
      <ul>
        { this.state.persons.map(person => <li>{person.isim}</li>)}
      </ul>
    )
  }
}