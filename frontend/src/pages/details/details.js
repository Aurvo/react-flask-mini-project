import React from 'react';
import {Link} from "react-router-dom";

class Details extends React.Component {
    state = {
        activeTab: 'Users',
        userData: "User Data",
        fileData: "File Data"
    }

    updateActiveTab(newTab) {
        this.setState({activeTab: newTab});
    }
    
    render() {
        const state = this.state;
        let paneContent;

        if (state.activeTab === 'Users') {
            paneContent = state.userData
        } else if (state.activeTab === 'Files') {
            paneContent = state.fileData
        }
        
        return (
            <div>
                <Link to="/">
                    <h4><i className="fas fa-angle-double-left"></i> Back</h4>
                </Link>
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

export default Details;