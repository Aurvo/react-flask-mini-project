import React from 'react';
import Table from './table';
import { textFilter } from 'react-bootstrap-table2-filter';

class ProjectsTableContainer extends React.Component {

        columns = [{
            dataField: 'id',
            text: 'Project ID',
            filter: textFilter(),
            sort: true
        }, {
            dataField: 'name',
            text: 'Project Name',
            filter: textFilter(),
            sort: true
        }, {
            dataField: 'start_date',
            text: 'Start Date',
            filter: textFilter(),
            sort: true
        }];
    
    render() {
        return <Table area="Project" columns={this.columns} />
    }
}

export default ProjectsTableContainer;