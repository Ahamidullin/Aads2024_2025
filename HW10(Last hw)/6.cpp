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
            for(auto &e:g[v]) if(e.cap && lvl[e.to]==-1){
                lvl[e.to]=lvl[v]+1; q.push(e.to);
            }
        }
        return lvl[t]!=-1;
    }
    long long dfs(int v,long long pushed){
        if(v==t || !pushed) return pushed;
        for(int &cid=ptr[v]; cid<(int)g[v].size(); ++cid){
            Edge &e=g[v][cid];
            if(e.cap && lvl[e.to]==lvl[v]+1){
                long long tr=dfs(e.to, min(pushed,e.cap));
                if(tr){ e.cap-=tr; g[e.to][e.rev].cap+=tr; return tr; }
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
    int n,m; long long w,b,gc;
    if(!(cin>>n>>m>>w>>b>>gc)) return 0;
    vector<string> a(n);
    for(auto &row:a) cin>>row;

    int V=n*m, S=V, T=V+1;
    Dinic din(V+2,S,T);

    auto id=[&](int i,int j){ return i*m+j; };

    for(int i=0;i<n;++i)
        for(int j=0;j<m;++j){
            int v=id(i,j);
            if(a[i][j]=='W'){
                din.add_edge(S,v,0);
                din.add_edge(v,T,b);
            }else{
                din.add_edge(S,v,w);
                din.add_edge(v,T,0);
            }
            const int di[4]={-1,0,1,0}, dj[4]={0,1,0,-1};
            for(int k=0;k<4;++k){
                int ni=i+di[k], nj=j+dj[k];
                if(ni>=0&&nj>=0&&ni<n&&nj<m){
                    int u=id(ni,nj);
                    din.add_edge(v,u,gc);
                }
            }
        }

    cout<<din.maxflow()<<"\n";
    return 0;
}
