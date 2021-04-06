

interface Todo {
    userId: number;
    id: number;
    title: string;
    completed: boolean;
}

class TutorialDataService {

    async http_get<T>( request: string ): Promise<T> {
        const response = await fetch(request);
        const body = await response.json();
        return body;
    }

    async allQuestion<T>( request: string ): Promise<T> {
        const body = this.http_get<T>(request)
        return body;
    }
    async question<T>( request:string, id: string ): Promise<T> {
        const body = this.http_get<T>(request+"/"+id)
        return body;
    }

    // async http_get<T>( request: string, ): Promise<T> {
    //     const body = this.http_get<T>(request)
    //     return body;
    // }

}

export default new TutorialDataService();