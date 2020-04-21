import React from 'react';
import Table from './table';
import { useParams } from 'react-router-dom'; 
import { textFilter } from 'react-bootstrap-table2-filter';

const columns = [{
    dataField: 'id',
    text: 'User ID',
    filter: textFilter(),
    sort: true
}, {
    dataField: 'name',
    text: 'Name',
    filter: textFilter(),
    sort: true
}, {
    dataField: 'email',
    text: 'Email Address',
    filter: textFilter(),
    sort: true
}, {
    dataField: 'project_id',
    text: 'Project Id',
    sort: true
}];
    
function UsersTableContainer() {
    const allwaysFilterObj = useParams();
    return <Table
        area="User"
        columns={columns}
        allwaysFilter={allwaysFilterObj}
    />
}

export default UsersTableContainer;