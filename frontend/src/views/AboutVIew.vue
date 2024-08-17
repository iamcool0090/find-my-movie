<template>
    <div class="about-us">
      <h1>About Us</h1>
      <p>
        We are a team of students from BMS College of Engineering (BMSCE). This project is a part of the Database Management Systems (DBMS) Advanced Applications and Techniques (AAT) course for Semester 4.
      </p>
      <section class="team">
        <h2>Our Team</h2>
        <ul>
          <li v-for="member in teamMembers" :key="member.id">
            <h3>{{ member.name }}</h3>
            <p>{{ member.role }}</p>
          </li>
        </ul>
      </section>
      <section class="project">
        <h2>About the Project</h2>
        <p>
          This project involves designing and implementing a database-driven application, showcasing our understanding and skills in database management, advanced queries, and application development.
        </p>
      </section>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        teamMembers: [
          { id: 1, name: 'Praful Chandra M', role: 'Project Lead' },
          { id: 2, name: 'Sathwik B C', role: 'Database Specialist' },
          { id: 3, name: 'Sai Gagan Sirigeri', role: 'Frontend Developer' },
        ]
      };
    }
  };
  </script>
  
  <style scoped>
  .about-us {
    padding: 20px;
    font-family: Arial, sans-serif;
  }
  
  h1, h2 {
    color: #333;
  }
  
  p {
    font-size: 16px;
    color: #666;
  }
  
  .team ul {
    list-style-type: none;
    padding: 0;
  }
  
  .team li {
    margin-bottom: 10px;
  }
  
  .team h3 {
    margin: 0;
    font-size: 18px;
  }
  
  .team p {
    margin: 5px 0 0;
    font-size: 14px;
    color: #888;
  }
  </style>
  