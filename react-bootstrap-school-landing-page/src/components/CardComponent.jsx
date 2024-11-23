// src/components/CardComponent.js
import React from 'react';
import { Card, Button } from 'react-bootstrap';

const CardComponent = ({ image, title, text, buttonText }) => {
  return (
    <Card className="mb-4 h-100">
      <Card.Img variant="top" src={image} />
      <Card.Body className="d-flex flex-column">
        <Card.Title>{title}</Card.Title>
        <Card.Text>{text}</Card.Text>
        <Button variant="primary" className="mt-auto">{buttonText}</Button>
      </Card.Body>
    </Card>
  );
}

export default CardComponent;
