import React from 'react';


const Posts = ({posts, loading}) => {
  if(loading){
    return <h2>loading posts...</h2>; // add spin wheel animation here
  }
  return (
        <div id="animal-content">
            <div className="col-md-6 col-xl-10 mx-auto p-0">
            
                <ul className="list-group list-group-flush">
                {posts.map(item => (
               
                <div>
                  <img alt="ANIMAL" className="profile_pic" src={item.image}></img>
                  <h2 style={{color: item.adoption_status === "AVAILABLE" ? "green": "red"}}>{item.adoption_status}</h2>
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

  );
};

 export default Posts;