import React from 'react';
import BootstrapTable from 'react-bootstrap-table-next';
import paginationFactory from 'react-bootstrap-table2-paginator';
import filterFactory, { textFilter, Comparator } from 'react-bootstrap-table2-filter';
import getData from '../axios/apiAdapter';


class Table extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            data: [],
            page: 1
        }
        this.sizePerPage = 5;
    }

    componentDidMount() {
        getData({
            table: this.props.area
        }, (response) => {
            this.setState({data: response.data});
        });
    }

    onTableChange = (type, newState) => {
    }
    
    render() {
        const state = this.state;
        return (
            <BootstrapTable
                keyField='id'
                data={state.data}
                columns={this.props.columns}
                bootstrap4
                remote={{
                    filter: true,
                    pagination: true,
                    sort: true,
                    cellEdit: false
                }}
                filter={ filterFactory() }
                pagination={paginationFactory({
                    page: state.page,
                    sizePerPage: this.sizePerPage,
                    totalSize: state.data.length
                })}
                onTableChange={this.onTableChange}
            />
        );
    }
}

export default Table;