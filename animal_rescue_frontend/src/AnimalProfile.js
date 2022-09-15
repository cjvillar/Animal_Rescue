import React, { Component } from 'react';

const Animals = [
  {
    "id": 1,
    "animal_type": "Bear",
    "name": "Teddy",
    "sex": "Male",
    "breed": "Black Bear",
    "neutred": false,
    "date_added": "2022-09-09T18:22:43.596807Z",
    "age": 5,
    "weight": "200 lbs",
    "adoption_status": "AVAILABLE",
    "temperament": "Mild",
    "likes": "Honey, Photographers",
    "fee": "5$",
    "location": "Alaska",
    "image": "http://127.0.0.1:8000/media/profile_images/teddy.JPG"
},
  
];

export class AnimalProfile extends Component {
  constructor(props) {
    super(props);
    this.state = {Animals};
  };

  render() {
    return(
        <main className="content">
        <div id="animal-content">
          {/* <div className="row"> */}
            <div className="col-md-6 col-xl-10 mx-auto p-0">
            
                <ul className="list-group list-group-flush">
                {this.state.Animals.map(item => (
                <div>
                  <img alt="HTML5" className="profile_pic" src={item.image}></img>
                  <h3 style={{color:"green"}}>{item.adoption_status}</h3>
                  <h1>{item.name}</h1>
                  <h3>Age: {item.age}</h3>
                  <h3>Weight: {item.weight}</h3>
                  <h3>Likes: {item.likes}</h3>
                  <h3>Fee: {item.fee}</h3>
                  <h3>location: {item.location}</h3>
                  
              </div>
              ))}
              </ul>
            </div>
          </div>
        {/* </div> */}
    
      </main>
    )
  }

}

export default AnimalProfile