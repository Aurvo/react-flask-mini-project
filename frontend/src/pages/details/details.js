import React from 'react';
import {Link, useParams } from 'react-router-dom';
import UsersTableContainer from '../../tables/usersTableContainer';
import FilesTableContainer from '../../tables/filesTableContainer';

class Details extends React.Component {
    state = {
        activeTab: 'Users',
    }

    updateActiveTab(newTab) {
        this.setState({activeTab: newTab});
    }
    
    render() {
        const state = this.state;
        let paneContent;

        if (state.activeTab === 'Users') {
            paneContent = <UsersTableContainer />
        } else if (state.activeTab === 'Files') {
            paneContent = <FilesTableContainer />
        }
        
        return (
            <div>
                <Link to="/">
                    <h4><i className="fas fa-angle-double-left"></i> Back</h4>
                </Link>
                <br></br>
                <DetailsHeader />
                <br></br>
                {/* Tabs */}
                <ul className="nav nav-tabs">
                    <li className="nav-item">
                        <a className={`nav-link ${state.activeTab === 'Users' ? 'active' : ''}`}
                        onClick={() => this.updateActiveTab('Users')} href="#">Users</a>
                    </li>
                    <li className="nav-item">
                        <a className={`nav-link ${state.activeTab === 'Files' ? 'active' : ''}`}
                        onClick={() => this.updateActiveTab('Files')} href="#">Files</a>
                    </li>
                </ul>

                {/* Panes */}
                <div className="tab-content">
                    <div className="tab-pane container-fluid active">{paneContent}</div>
                </div>
            </div>
        );
    }
}

//need to make a separate functional component for thei becasue it uses a react hook
function DetailsHeader() {
    const urlParams = useParams();
    const appendedToHeader = urlParams && urlParams.project_name ?
         ` for ${urlParams.project_name}` : '';
    return <h1>Details{appendedToHeader}</h1>
}

export default Details;