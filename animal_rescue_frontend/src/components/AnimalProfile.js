import React from 'react';

const Posts = ({ posts, loading }) => {
  if (loading) {
    return <h2>Loading Posts...</h2>; // add spin wheel animation here
  }
  return (
    <div className="container mt-5">
      <div className="row">
        {posts.map((item) => (
          <div className="container d-flex justify-content-center">
            <div className="card">
              <img
                className="card-img-top "
                src={item.image}
                alt="Animal"
                width="400" 
                height="400"
              />
              <div className="card-body">
                <h2
                  className={`card-title mb-3 ${
                    item.adoption_status === 'AVAILABLE' ? 'text-success' : 'text-danger'
                  }`}
                >
                  {item.adoption_status}
                </h2>
                <h1 className="card-subtitle mb-2">{item.name}</h1>
                <p className="card-text mb-2">
                  Age: {item.age} | Weight: {item.weight}
                </p>
                <p className="card-text mb-2">Likes: {item.likes}</p>
                <p className="card-text mb-2">Fee: {item.fee}</p>
                <p className="card-text mb-2">Location: {item.location}</p>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Posts;
