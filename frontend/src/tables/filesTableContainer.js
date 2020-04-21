import React from 'react';
import Table from './table';
import { useParams } from 'react-router-dom'; 
import { textFilter } from 'react-bootstrap-table2-filter';

const columns = [{
    dataField: 'id',
    text: 'File ID',
    filter: textFilter(),
    sort: true
}, {
    dataField: 'name',
    text: 'File Name',
    filter: textFilter(),
    sort: true
}, {
    dataField: 'type',
    text: 'File Type',
    filter: textFilter(),
    sort: true
}, {
    dataField: 'project_id',
    text: 'Project Id',
    sort: true
}];
    
function FilesTableContainer() {
    const allwaysFilterObj = useParams();
    return <Table
        area="File"
        columns={columns}
        allwaysFilter={allwaysFilterObj}
    />
}

export default FilesTableContainer;