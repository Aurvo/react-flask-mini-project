import React from 'react';


class Table extends React.Component {
    render() {
        const props = this.props;
        return (
            <BootstrapTable keyField='id' data={props.data} columns={props.columns}/>
        );
    }
}

export default Table;