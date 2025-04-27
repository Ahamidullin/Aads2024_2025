#include <bits/stdc++.h>
using namespace std;

struct Edge{int to, rev; long long cap;};

struct Dinic{
    int n, s, t; vector<vector<Edge>> g; vector<int> lvl, ptr;
    Dinic(int n,int s,int t):n(n),s(s),t(t),g(n),lvl(n),ptr(n){}
    void add_edge(int v,int to,long long cap){
        Edge a{to,(int)g[to].size(),cap}, b{v,(int)g[v].size(),0};
        g[v].push_back(a); g[to].push_back(b);
    }
    bool bfs(){
        fill(lvl.begin(),lvl.end(),-1);
        queue<int> q; lvl[s]=0; q.push(s);
        while(!q.empty()){
            int v=q.front(); q.pop();
            for(auto &e:g[v]) if(e.cap&&lvl[e.to]==-1){
                lvl[e.to]=lvl[v]+1; q.push(e.to);
            }
        }
        return lvl[t]!=-1;
    }
    long long dfs(int v,long long pushed){
        if(v==t||!pushed) return pushed;
        for(int &cid=ptr[v];cid<(int)g[v].size();++cid){
            Edge &e=g[v][cid];
            if(e.cap&&lvl[e.to]==lvl[v]+1){
                long long tr=dfs(e.to,min(pushed,e.cap));
                if(tr){e.cap-=tr; g[e.to][e.rev].cap+=tr; return tr;}
            }
        }
        return 0;
    }
    long long maxflow(){
        long long flow=0;
        while(bfs()){
            fill(ptr.begin(),ptr.end(),0);
            while(long long pushed=dfs(s,LLONG_MAX)) flow+=pushed;
        }
        return flow;
    }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n,m; if(!(cin>>n>>m)) return 0;
    Dinic dinic(n,0,n-1);
    for(int i=0;i<m;++i){
        int u,v; long long c; cin>>u>>v>>c;
        dinic.add_edge(u-1,v-1,c);
    }
    cout<<dinic.maxflow()<<"\n";
    return 0;
}
