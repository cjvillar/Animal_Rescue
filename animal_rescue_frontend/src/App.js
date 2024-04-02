import React, { useState, useEffect } from "react";
import axios from "axios";
import "./App.css";
import AnimalProfile from "./components/AnimalProfile.js";
import Pagination from "./components/Pagination";
import Navbar from "react-bootstrap/Navbar";
import Register from "./components/Register";
import Login from "./components/Login";
import Logout from "./components/Logout";
import { Button, Container} from "react-bootstrap";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";
axios.defaults.withCredentials = true;

const client = axios.create({
  baseURL: "http://0.0.0.0:8000",
});

const App = () => {
  const [currentUser, setCurrentUser] = useState();
  const [registrationToggle, setRegistrationToggle] = useState(false);
  const [email, setEmail] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(false);
  const [currentPage, setCurrentPage] = useState(1);
  const [postPerPage] = useState(1);

  //change page
  const paginate = (pageNumber) => setCurrentPage(pageNumber);

  //Get current animal
  const indexOfLastPost = currentPage * postPerPage;
  const indexOfFirstPost = indexOfLastPost - postPerPage;
  const currentPosts = posts.slice(indexOfFirstPost, indexOfLastPost);

  useEffect(() => {
    client
      .get("api/register")
      .then(function (res) {
        setCurrentUser(true);
      })
      .catch(function (error) {
        setCurrentUser(false);
      });
  }, []);

  function update_form_btn() {
    if (registrationToggle) {
      document.getElementById("form_btn").innerHTML = "Register";
      setRegistrationToggle(false);
    } else {
      document.getElementById("form_btn").innerHTML = "Log in";
      setRegistrationToggle(true);
    }
  }

  function submitLogout() {
    setCurrentUser(false);
  }

  useEffect(() => {
    const fetchPosts = async () => {
      setLoading(true);
      const res = await axios.get("http://0.0.0.0:8000/api/animal_rescue_api/");
      setPosts(res.data);
      setLoading(false);
    }

    fetchPosts();
  }, []);

  return (
    <div>
      <Navbar bg="grey" variant="grey">
        <Container>
          <Navbar.Brand>ANIMAL RESCUE <img
          alt=""
          src="./Black_Paw.svg"
          width="30"
          height="30"
          className="d-inline-block align-top"
        />{' '}</Navbar.Brand>
          <Navbar.Toggle />
          <Navbar.Collapse className="justify-content-end">
            <Navbar.Text>
              {currentUser ? (
                <Logout onSuccess={submitLogout} baseUrl={client.defaults.baseURL}/>
              ) : (
                <Button id="form_btn" onClick={update_form_btn} variant="light">
                  Register
                </Button>
              )}
            </Navbar.Text>
          </Navbar.Collapse>
        </Container>
      </Navbar>
      {!currentUser && (
        <div className="center">
          {registrationToggle ? (
            <Register onSuccess={() => setCurrentUser(true)} baseUrl={client.defaults.baseURL} />
          ) : (
            <Login onSuccess={() => setCurrentUser(true)} baseUrl={client.defaults.baseURL} />
          )}
        </div>
      )}
      {currentUser && (
        <div>
          <div className="center">
            <h2>You're logged in!</h2>
          </div>
          <AnimalProfile posts={currentPosts} loading={loading} />
          <br></br>
          <Pagination
            PostsPerPage={postPerPage}
            totalPosts={posts.length}
            paginate={paginate}
          />
        </div>
      )}
    </div>
  );
};

export default App;

