// src/App.js
import React from 'react';
import { Container, Row, Col } from 'react-bootstrap';
import NavbarComponent from './components/NavbarComponent';
import CardComponent from './components/CardComponent';

function App() {
  return (
    <>
      <NavbarComponent />

      <Container className="mt-5">
        <Row className="mb-4 text-center">
          <Col>
            <h1>Welcome to Our School</h1>
            <p>Providing quality education since [Year]</p>
          </Col>
        </Row>

        <Row>
          <Col xs={12} md={4}>
            <CardComponent 
              image="https://via.placeholder.com/150"
              title="Our Programs"
              text="Learn about the various programs we offer to support students' growth and development."
              buttonText="Learn More"
            />
          </Col>
          <Col xs={12} md={4}>
            <CardComponent 
              image="https://via.placeholder.com/150"
              title="Admissions"
              text="Find out how to apply and join our community of learners."
              buttonText="Apply Now"
            />
          </Col>
          <Col xs={12} md={4}>
            <CardComponent 
              image="https://via.placeholder.com/150"
              title="Contact Us"
              text="Get in touch with us for any queries or information you need."
              buttonText="Contact"
            />
          </Col>
        </Row>
      </Container>
    </>
  );
}

export default App;
