// Logout.js

import React from "react";
import { Button } from "react-bootstrap";
import axios from "axios";

const Logout = ({ onSuccess, baseUrl }) => {
  const handleLogout = async () => {
    try {
      await axios.post(`${baseUrl}/api/logout`);
      onSuccess();
    } catch (error) {
      console.error("Logout error:", error);
    }
  };

  return (
    <Button onClick={handleLogout} variant="light">
      Log out
    </Button>
  );
};

export default Logout;
