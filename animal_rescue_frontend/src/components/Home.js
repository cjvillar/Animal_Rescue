import React, { useState, useEffect } from "react";
import axios from 'axios'
import Pagination from './Pagination.js'
import AnimalProfile from './AnimalProfile.js';


const Home = () => {
    const [posts, setPosts] = useState([]);
    const [loading, setLoading] = useState(false);
    const [currentPage, setCurrentPage] = useState(1);
    const [postPerPage] = useState(1);
    
    //change page
    const paginate = (pageNumber) => setCurrentPage(pageNumber);
  
    useEffect(() => {
      const fetchPosts = async () => {
        setLoading(true);
        const res = await axios.get("http://127.0.0.1:8000/api/animal_rescue_api/");
        setPosts(res.data);
        setLoading(false);
      }
  
      fetchPosts();
    }, []);
    //Get current animal
    const indexOfLastPost = currentPage * postPerPage;
    const indexOfFirstPost = indexOfLastPost - postPerPage;
    const currentPosts = posts.slice(indexOfFirstPost,indexOfLastPost);  
  return (

      <div>

        <AnimalProfile posts={currentPosts} loading={loading} />
        <Pagination PostsPerPage={postPerPage} totalPosts={posts.length} paginate={paginate}/>

    </div>
 
  )
}

export default Home