import React from 'react';
import ProjectsTableContainer from '../../tables/projectsTableContainer';

class Home extends React.Component {
    
    render() {
        return (<div>
            <h1>Projects</h1>
            <br></br>
            <ProjectsTableContainer/>
        </div>);
    }
}

export default Home;