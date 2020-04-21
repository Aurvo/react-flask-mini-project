import React from 'react';
import BootstrapTable from 'react-bootstrap-table-next';
import paginationFactory from 'react-bootstrap-table2-paginator';
import filterFactory, { textFilter, Comparator } from 'react-bootstrap-table2-filter';
import getDataForReal from '../axios/apiAdapter';


class Table extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            data: [],
            page: 1
        }
        this.sizePerPage = 5;
    }

    
    // requests data from the backend, but makes sure certain fields are
    // allways filtered based on the allwaysFilter prop
    getData(params, callback) {
        const allwaysFilter = this.props.allwaysFilter;
        if (this.props.allwaysFilter) {
            for (let field in allwaysFilter) {
                params[field] = allwaysFilter[field];
            }
        }
        getDataForReal(params, callback);
    }
    
    // requests data from backend upon mounting
    componentDidMount() {
        this.getData({
            area: this.props.area
        }, response => {
            this.setState({data: response.data});
        });
    }

    onTableChange = (type, newState) => {
        console.log(type);
        console.log(newState);
        
        // capture filters
        const filterFields = [];
        const filterValues = [];
        const filters = newState.filters;
        for (let field in newState.filters) {
            filterFields.push(field);
            filterValues.push(filters[field].filterVal);
        }

        this.getData({
            area: this.props.area,
            order_by: newState.sortedField,
            desc: newState.sortOrder === 'desc',
            fields: filterFields,
            values: filterValues,
            page: newState.page,
            rows_per_page: newState.sizePerPage
        }, response => {
            this.setState({data: response.data});
        });
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