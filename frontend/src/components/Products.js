import React from "react";
import Table from "react-bootstrap/Table";
import axios from "axios";

export default class Products extends React.Component {
  state = {
    products: [],
  };

  componentDidMount() {
    axios.get(`http://127.0.0.1:8000/api/urunler/`).then((res) => {
      const products = res.data;
      this.setState({ products });
    });
  }

  render() {
    return (
      <Table striped bordered hover variant="dark">
        <thead>
          <tr>
            <th>#</th>
            <th>First Name</th>
            <th>Last Name</th>
            <th>Username</th>
          </tr>
        </thead>
        <tbody>
          {this.state.products.map((product) => {
            return product.satici.isim === "Default" ? (
              <tr>
                <td>{product.id}</td>
                <td>{product.isim}</td>
                <td>{product.fiyat}</td>
                <td>{product.satici.isim}</td>
              </tr>
            ) : null;
          })}
        </tbody>
      </Table>
    );
  }
}
