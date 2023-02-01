import React, { useState, useEffect } from "react";
import { BrowserRouter, Routes, Route} from 'react-router-dom'
import './App.css';
// import AnimalProfile from './components/AnimalProfile.js';
import Banner from './components/Banner.js';
// import axios from 'axios'
// import Pagination from './components/Pagination'
import LoginPage from "./components/LoginPage";
import Home from "./components/Home"
import PrivateRoute from './utils/privateRoutes'


const App = () => {
  // const [posts, setPosts] = useState([]);
  // const [loading, setLoading] = useState(false);
  // const [currentPage, setCurrentPage] = useState(1);
  // const [postPerPage] = useState(1);
  
  // //change page
  // const paginate = (pageNumber) => setCurrentPage(pageNumber);

  // useEffect(() => {
  //   const fetchPosts = async () => {
  //     setLoading(true);
  //     const res = await axios.get("http://127.0.0.1:8000/api/animal_rescue_api/");
  //     setPosts(res.data);
  //     setLoading(false);
  //   }

  //   fetchPosts();
  // }, []);
  // //Get current animal
  // const indexOfLastPost = currentPage * postPerPage;
  // const indexOfFirstPost = indexOfLastPost - postPerPage;
  // const currentPosts = posts.slice(indexOfFirstPost,indexOfLastPost);
  
  return (
    <div className='container mt-5'>
      
      <BrowserRouter>
      <div>
        <Banner />
        <Routes>
          <Route element={<LoginPage/>} path='/' exact/>
          <Route element={<PrivateRoute/>} >
            <Route element={<Home />} path='/*' />
          </Route>

          {/* <Route element={<AnimalProfile />} posts={currentPosts} loading={loading} path='/AnimalProfile'/> */}
        </Routes>
      </div>
      {/* <Pagination PostsPerPage={postPerPage} totalPosts={posts.length} paginate={paginate}/> */}
      </BrowserRouter>
      {/* <AnimalProfile posts={currentPosts} loading={loading} /> */}
     
    </div>

  );

};
  
export default App;