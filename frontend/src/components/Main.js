import React from 'react';
import {useQuery, useMutation} from '@apollo/react-hooks';
import {gql} from 'apollo-boost';

function Main() {
    const {data} = useQuery(gql`
        {
          user(id: 16) {
              id
              username
          }
        }
    `);
    const MUTATION = gql`
        mutation mutation($id: Int, $role: Int, $username: String, $type: String!) {
            userMutation(id: $id, role: $role, username: $username, type: $type) {
                user {
                    id
                    role
                    type
                    username
                }         
            }
        }
    `;
    const [userMutation, {data: d}] = useMutation(MUTATION);

    if (data.user && data.user.length === 0) {
        return <p>没有数据。</p>
    }

    let usernameInput;
    let roleInput;
    return (
        <div className="App">
            {data.user && data.user.length > 0 && data.user.map(item => {
                let input;
                return <div key={item.id}>
                    <p>{item.id} {item.username}</p>
                    <form
                        onSubmit={e => {
                            e.preventDefault();
                            userMutation({ variables: { id: Number(item.id), role: Number(input.value), type: 'update' } });
                            input.value = '';
                        }}
                    >
                        <input
                            ref={node => input = node}
                        />
                        <button type="submit">Update</button>
                    </form>
                </div>
            })}
            <form
                onSubmit={e => {
                    e.preventDefault();
                    userMutation({ variables: { username: usernameInput.value, role: Number(roleInput.value), type: 'create' } });
                    usernameInput.value = '';
                    roleInput.value = '';
                }}
            >
                <input
                    placeholder="name"
                    ref={node => usernameInput = node}
                />
                <input
                    placeholder="role"
                    ref={node => roleInput = node}
                />
                <button type="submit">Create</button>
            </form>
            <form
                onSubmit={e => {
                    e.preventDefault();
                    userMutation({ variables: { id: Number(usernameInput.value), type: 'delete' } });
                    usernameInput.value = '';
                    roleInput.value = '';
                }}
            >
                <input
                    placeholder="id"
                    ref={node => usernameInput = node}
                />
                <button type="submit">Delete</button>
            </form>
            {d && <p>成功！</p>}
        </div>
    );
}

export default Main;
