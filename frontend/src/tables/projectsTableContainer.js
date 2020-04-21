import React from 'react';
import Table from './table';

class ProjectsTableContainer extends React.Component {
    data = [3];

    render() {
        const state = this.state;
        return <Table data={data} />>
    }
}

export default ProjectsTableContainer;